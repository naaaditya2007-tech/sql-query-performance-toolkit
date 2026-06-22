import math

def estimate_query_plan(rows: int, indexed: bool) -> dict:
    if indexed:
        cost = round(math.log2(max(rows, 2)) * 1.5, 2)
        plan = "INDEX_SCAN"
    else:
        cost = float(rows)
        plan = "SEQ_SCAN"
    return {"rows": rows, "plan": plan, "io_cost": cost}

if __name__ == "__main__":
    print("Unindexed:", estimate_query_plan(50000, False))
    print("Indexed:", estimate_query_plan(50000, True))
