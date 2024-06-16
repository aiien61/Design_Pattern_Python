import logging
from abc import ABC, abstractmethod
from typing import List, Any, Optional

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Agent(ABC):
    @abstractmethod
    def get_task(self, *args, **kwargs): raise NotImplementedError


class Center(ABC):
    @abstractmethod
    def register_agent(self): raise NotImplementedError
    @abstractmethod
    def remove_agent(self): raise NotImplementedError
    @abstractmethod
    def notify_agents(self): raise NotImplementedError


class Event(list):
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        for item in self:
            item(*args, **kwargs)


class JobCenter(Center):
    
    def __init__(self) -> None:
        self.resource_center: Optional[Center] = None
        self.job_name: Optional[str] = None
        self.due_time: Optional[int] = None

    def register_agent(self, rc: Center):
        self.resource_center = rc

    def remove_agent(self):
        self.resource_center = None

    def notify_agents(self):
        self.resource_center.send_a_task(self)

    @property
    def best_est_time(self) -> Optional[tuple]:
        return self.resource_center.report_est_time()

    def set_a_job(self, job_name: str, due_time: int):
        self.job_name = job_name
        self.due_time = due_time
        self.job_changed()

    def job_changed(self):
        self.notify_agents()

    def clear(self):
        self.job_name = None
        self.due_time = None


class ResourceCenter(Center):
    def __init__(self, jc: JobCenter = None) -> None:
        self.job_info: dict = {}
        self.job_center: Optional[JobCenter] = jc
        self.resource_agents: List = []

        if jc:
            jc.register_agent(self)

    def register_agent(self, resource: Agent) -> bool:
        self.resource_agents.append(resource)

    def remove_agent(self, resource: Agent) -> bool:
        self.resource_agents.remove(resource)
        return True

    def notify_agents(self) -> None:
        for agent in self.resource_agents:
            agent.get_task(self)
        return None

    def send_a_task(self, center: Center) -> None:
        self.job_info['job_name'] = center.job_name
        self.job_info['due_time'] = center.due_time
        self.notify_agents()
        return None
    
    def update_resource_available_time(self, resource_agent: Agent, used_time: int) -> bool:
        update_done: bool = False
        try:
            resource_agent.update_available_time(used_time)
        except KeyError as e:
            logging.debug(e)
        except ValueError as e:
            logging.debug(e)
        else:
            update_done = True
        finally:
            return update_done

    def report_est_time(self) -> Optional[tuple]:
        end_time_list: list = []
        for ra in self.resource_agents:
            end_time = ra.return_end_time()
            if end_time is None:
                continue
            end_time_list.append((ra, end_time))

        try:
            return max(end_time_list, key=lambda x: x[1])
        except ValueError as e:
            logging.debug(e)
            return None


class MachineAgent(Agent):
    def __init__(self, jc: Optional[ResourceCenter] = None, available_time: List = None):
        self.resource_center: Optional[ResourceCenter] = jc
        self.due_time: Optional[int] = None
        self.available_time: List = [] if available_time is None else available_time

        if jc:
            jc.register_agent(self)

    def get_task(self, center: Center) -> bool:
        get_task_done: bool = False
        try:
            self.due_time = center.job_info['due_time']
        except KeyError as e:
            logging.debug(e)
        else:
            get_task_done = True
        finally:
            return get_task_done 

    def return_end_time(self):
        return self.calculate_best_end_time()

    def calculate_best_end_time(self) -> Optional[int]:
        max_end_time: Optional[int] = None
        for time in self.available_time:
            if time > self.due_time:
                continue

            if max_end_time is None:
                max_end_time = time
            else:
                if time > max_end_time:
                    max_end_time = time
        return max_end_time
    
    def update_available_time(self, used_time: int) -> bool:
        get_update_done: bool = False
        try:
            self.available_time.remove(used_time)
        except KeyError as e:
            logging.debug(e)
        else:
            get_update_done = True
        finally:
            return get_update_done


class SchedulerCenter(Center):

    def __init__(self, jc: JobCenter, rc: ResourceCenter) -> None:
        self.job_center = jc
        self.resource_center = rc

    def register_agent(self, center: Center):
        if isinstance(center, JobCenter):
            self.job_center = center
        elif isinstance(center, ResourceCenter):
            self.resource_center = center

    def remove_agent(self, center: Center):
        if isinstance(center, JobCenter):
            self.job_center = None
        elif isinstance(center, ResourceCenter):
            self.resource_center = None
    
    def notify_agents(self, center: Center, *args, **kwargs):
        if isinstance(center, JobCenter):
            self.job_center.set_a_job(*args, **kwargs)
        elif isinstance(center, ResourceCenter):
            self.resource_center.update_resource_available_time(*args, **kwargs)

    def check_job_done(self):
        job_end_time: Optional[tuple] = self.job_center.best_est_time
        if job_end_time is None:
            return False
        return True
    
    def perform_a_job(self, **job) -> bool:
        self.notify_agents(self.job_center, **job)
        if self.check_job_done():
            resource_agent, used_time = self.job_center.best_est_time
            self.notify_agents(self.resource_center, resource_agent, used_time)
            self.job_center.clear()
            return True
        return False
        

def scheduling():
    job_center: JobCenter = JobCenter()
    
    resource_center: ResourceCenter = ResourceCenter(job_center)

    scheduler: SchedulerCenter = SchedulerCenter(jc=job_center, rc=resource_center)

    machine1: MachineAgent = MachineAgent(resource_center, [1, 2, 3, 4, 5])
    machine2: MachineAgent = MachineAgent(resource_center, [1, 3, 5, 7, 9])

    job1 = {'job_name': 'carwash', 'due_time': 5}
    scheduler.perform_a_job(**job1)
    logging.debug(f'After job1, machine1 left: {machine1.available_time}')
    logging.debug(f'After job1, machine2 left: {machine2.available_time}')

    job2 = {'job_name': 'dishwash', 'due_time': 7}
    scheduler.perform_a_job(**job2)
    logging.debug(f'After job2, machine1 left: {machine1.available_time}')
    logging.debug(f'After job2, machine2 left: {machine2.available_time}')



if __name__ == '__main__':
    scheduling()

