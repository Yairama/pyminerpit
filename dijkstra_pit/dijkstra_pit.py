import numpy as np
import os
from numpy import inf
from IPython.core.display import display


def parse_data():
    print('************************************************************')
    print("PRIMARY REVENUE BLOCK MODEL:")
    file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data/Datalog.csv'))

    (name_file, type_file) = file.split('g.')
    file_data = None
    if type_file == 'txt':
        file_data = np.loadtxt(file, delimiter='\t', skiprows=0)
    elif type_file == 'csv':
        file_data = np.loadtxt(file, delimiter=',', skiprows=0)
    else:
        print('-----------file not defined-------')
        exit()

    print(file_data)
    return file_data


def create_cumulative_block(data_):
    print('************************************************************')
    print("CUMULATIVE REVENUE BLOCK MODEL:")
    rows, columns = data_.shape
    cumulative = data_

    for row_index in range(rows):

        if row_index == 0:
            continue

        for index in range(columns):
            cumulative[row_index][index] = cumulative[row_index][index] + cumulative[row_index - 1][index]

    print(cumulative)
    return cumulative


def create_simulated_block_model(cumulative_block_):
    rows, columns = cumulative_block_.shape
    vertices_size = (rows + 1) * (columns + 1)

    print('************************************************************')
    print("COMPUTING GRAPH:")

    graph = {}

    for row in range(rows + 1):

        for column in range(columns + 1):

            key = str(row) + "-" + str(column)

            if row == 0:
                if column == 0:

                    d_line = str(row + 1) + "-" + str(column + 1)
                    graph[key] = {d_line: cumulative_block_[0][column]}

                if column == columns:

                    d_line = str(row + 1) + "-" + str(column - 1)
                    graph[key] = { d_line: 0}

            if row == rows:
                if column == 0:
                    h_line = str(row) + "-" + str(column + 1)
                    d_line = str(row - 1) + "-" + str(column + 1)
                    graph[key] = {h_line: cumulative_block_[row - 1][0], d_line: cumulative_block_[row - 2][0]}

                if column == columns:
                    h_line = str(row) + "-" + str(column - 1)
                    d_line = str(row - 1) + "-" + str(column - 1)
                    graph[key] = {h_line: cumulative_block_[row - 1][column - 1],
                                  d_line: cumulative_block_[row - 1][column - 1]}

            if column != 0 and column != columns:
                if row == 0:

                    d_l_line = str(row + 1) + "-" + str(column - 1)
                    d_r_line = str(row + 1) + "-" + str(column + 1)
                    graph[key] = {
                                  d_l_line: 0, d_r_line: cumulative_block_[row][column]}

                if row == rows:
                    h_l_line = str(row) + "-" + str(column - 1)
                    h_r_line = str(row) + "-" + str(column + 1)
                    d_l_line = str(row - 1) + "-" + str(column - 1)
                    d_r_line = str(row - 1) + "-" + str(column + 1)
                    graph[key] = {h_l_line: cumulative_block_[row - 1][column - 1],
                                  h_r_line: cumulative_block_[row - 1][column],
                                  d_l_line: cumulative_block_[row - 1][column - 1],
                                  d_r_line: cumulative_block_[row - 2][column]}

            if row != 0 and row != rows:
                if column == 0:
                    h_line = str(row) + "-" + str(column + 1)
                    d_u_line = str(row - 1) + "-" + str(column + 1)
                    d_d_line = str(row + 1) + "-" + str(column + 1)
                    graph[key] = {h_line: cumulative_block_[row - 1][column],
                                  d_u_line: 0 if row - 2 < 0 else cumulative_block_[row - 2][column],
                                  d_d_line: cumulative_block_[row][column]}

                if column == columns:
                    h_line = str(row) + "-" + str(column - 1)
                    d_u_line = str(row - 1) + "-" + str(column - 1)
                    d_d_line = str(row + 1) + "-" + str(column - 1)
                    graph[key] = {h_line: cumulative_block_[row - 1][column - 1],
                                  d_u_line: cumulative_block_[row - 1][column - 1],
                                  d_d_line: cumulative_block_[row - 1][column - 1]}

            if row != 0 and row != rows and column != 0 and column != columns:
                h_l_line = str(row) + "-" + str(column - 1)
                h_r_line = str(row) + "-" + str(column + 1)
                d_l_u_line = str(row - 1) + "-" + str(column - 1)
                d_r_u_line = str(row - 1) + "-" + str(column + 1)
                d_l_d_line = str(row + 1) + "-" + str(column - 1)
                d_r_d_line = str(row + 1) + "-" + str(column + 1)
                graph[key] = {h_l_line: cumulative_block_[row - 1][column - 1],
                              d_l_u_line: cumulative_block_[row - 1][column - 1],
                              d_l_d_line: cumulative_block_[row - 1][column - 1],
                              h_r_line: cumulative_block_[row - 1][column],
                              d_r_u_line: 0 if row - 2 < 0 else cumulative_block_[row - 2][column],
                              d_r_d_line: cumulative_block_[row][column]}

    for connection in graph:
        print(connection, ':', graph[connection])

    return graph


def calculate_costs(r_,c_):
    costs = {}
    for row in range(r+1):
        for column in range(c+1):
            if row == 0 and column == 0:
                costs[str(row)+'-'+str(column)] = 0
            else:
                costs[str(row)+'-'+str(column)] = -inf

    return costs


def search(source, target, graph, costs, parents):
    nextNode = source

    while nextNode != target:
        nn = nextNode.split("-")
        for neighbor in graph[nextNode]:
            nb = neighbor.split("-")
            if graph[nextNode][neighbor] + costs[nextNode] >= costs[neighbor] and nb[1]>=nn[1]:
                costs[neighbor] = graph[nextNode][neighbor] + costs[nextNode]
                # print("NEXT NODE:", nextNode)
                # print("COST NEXT NODE:", costs[nextNode])
                parents[neighbor] = nextNode

            del graph[neighbor][nextNode]

        del costs[nextNode]
        nextNode = max(costs, key=costs.get)

    return parents


def backpedal(source, target, searchResult):
    node = target

    backpath = [target]

    path = []

    while node != source:
        backpath.append(searchResult[node])

        node = searchResult[node]

    for i in range(len(backpath)):
        path.append(backpath[-i - 1])

    return path


if __name__ == '__main__':
    data = parse_data()
    cumulative_block = create_cumulative_block(data)
    __graph = create_simulated_block_model(cumulative_block)
    r, c = cumulative_block.shape

    __costs = calculate_costs(r,c)
    __parents = {}
    result = search('0-0', str(0)+'-'+str(c), __graph, __costs, __parents)

    print('************************************************************')
    print("RESULTS:")
    print('parent dictionary={}'.format(result))
    print('Optimum Pit Vertices path={}'.format(backpedal('0-0', str(0)+'-'+str(c), result)))
