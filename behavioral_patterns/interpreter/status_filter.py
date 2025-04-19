# 抽象語法節點
class Expression:
    def interpret(self, context):
        pass

# 終端表達式：欄位比較
class EqualsExpression(Expression):
    def __init__(self, field, value):
        self.field = field
        self.value = value
    
    def interpret(self, context):
        return str(context.get(self.field)) == self.value

class GreaterThanExpression(Expression):
    def __init__(self, field, value):
        self.field = field
        self.value = float(value)
    
    def interpret(self, context):
        return float(context.get(self.field)) > self.value

# 非終端表達式：AND / OR
class AndExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self, context):
        return self.left.interpret(context) and self.right.interpret(context)

class OrExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self, context):
        return self.left.interpret(context) or self.right.interpret(context)

# 假設語法格式簡單：field op value [and/or field op value]
def parse_expression(expression_str):
    tokens = expression_str.strip().split()
    left_expr = parse_single(tokens[0], tokens[1], tokens[2])

    if len(tokens) == 3:
        return left_expr
    elif tokens[3] == "and":
        right_expr = parse_single(tokens[4], tokens[5], tokens[6])
        return AndExpression(left_expr, right_expr)
    elif tokens[3] == "or":
        right_expr = parse_single(tokens[4], tokens[5], tokens[6])
        return OrExpression(left_expr, right_expr)

def parse_single(field, op, value):
    value = value.strip('"')  # 移除引號
    if op == "==":
        return EqualsExpression(field, value)
    elif op == ">":
        return GreaterThanExpression(field, value)
    else:
        raise ValueError(f"不支援的操作符：{op}")

if __name__ == "__main__":
    orders = [
        {"order_id": "A01", "status": "waiting", "product": "X", "batch_size": 150},
        {"order_id": "A02", "status": "done", "product": "A01", "batch_size": 80},
        {"order_id": "A03", "status": "waiting", "product": "A01", "batch_size": 130}
    ]

    query = 'status == "waiting" and batch_size > 100'
    expr = parse_expression(query)

    print(f"🔍 查詢語法：{query}")
    for order in orders:
        if expr.interpret(order):
            print(f"✅ 符合條件：{order}")
