

def main():
    malloc_optimize()


def malloc_optimize():
    budget = 1
    cost_wall = 0
    wall = [0, 0, 0]
    while cost_wall <= budget:
        cost_wall = calc_construction_cost(wall)
        surge = run_gissr(wall)
        cost_damage = calc_damage_cost(surge)
        record_solution(wall, cost_wall, cost_damage, surge)
        



if __name__ == "__main__":
    main()
