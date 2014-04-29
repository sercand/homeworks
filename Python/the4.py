#Created by Sercan Degirmenci on 22.01.2014
label_index, tree_nw, tree_ne, tree_sw, tree_se, default, first_value = 0, 1, 4, 2, 3, 0, 1
node_data, node_is_tree, node_nw, node_ne, node_sw, node_se, node_width, node_height = 0, 1, 2, 5, 3, 4, 1, 2

def get_label(obj):
    return obj[label_index] if type(obj) is list else obj

def is_tree(obj):
    return False if type(obj) is not list else len(obj) > 3

def change_data(value, data, node):
    if node[node_data][data] is value: return
    node[node_data][data] = value
    if node[node_is_tree]:
        if data is node_width:
            if node[node_nw][node_data][data] > default:
                change_data(value-node[node_nw][node_data][data], data, node[node_ne])
                change_data(value-node[node_nw][node_data][data], data, node[node_se])
            elif node[node_ne][node_data][data] > default:
                change_data(value-node[node_ne][node_data][data], data, node[node_nw])
                change_data(value-node[node_ne][node_data][data], data, node[node_sw])
        else:
            if node[node_ne][node_data][data] > default:
                change_data(value-node[node_ne][node_data][data], data, node[node_se])
                change_data(value-node[node_ne][node_data][data], data, node[node_sw])
            elif node[node_se][node_data][data] > default:
                change_data(value-node[node_se][node_data][data], data, node[node_nw])
                change_data(value-node[node_se][node_data][data], data, node[node_ne])

def solve(tree, result):
    label = get_label(tree)
    res_data = [label, default, default]
    node = [res_data, False, None, None, None, None]
    result.append(res_data)
    if not is_tree(tree):
        node[node_is_tree] = False
        if type(tree) is list:
            for i in xrange(first_value, len(tree)):
                if tree[i] > default:
                    res_data[node_width] = tree[i]
                else:
                    res_data[node_height] = -tree[i]
    else:
        node[node_is_tree] = True
        node[node_nw], node[node_sw] = solve(tree[tree_nw], result), solve(tree[tree_sw], result)
        node[node_se], node[node_ne] = solve(tree[tree_se], result), solve(tree[tree_ne], result)
        if node[node_nw][node_data][node_width] > default:
            change_data(node[node_nw][node_data][node_width], node_width, node[node_sw])
        elif node[node_sw][node_data][node_width] > default:
            change_data(node[node_sw][node_data][node_width], node_width, node[node_nw])
        if node[node_ne][node_data][node_width] > default:
            change_data(node[node_ne][node_data][node_width], node_width, node[node_se])
        elif node[node_se][node_data][node_width] > default:
            change_data(node[node_se][node_data][node_width], node_width, node[node_ne])
        if node[node_ne][node_data][node_height] > default:
            change_data(node[node_ne][node_data][node_height], node_height, node[node_nw])
        elif node[node_nw][node_data][node_height] > default:
            change_data(node[node_nw][node_data][node_height], node_height, node[node_ne])
        if node[node_se][node_data][node_height] > default:
            change_data(node[node_se][node_data][node_height], node_height, node[node_sw])
        elif node[node_sw][node_data][node_height] > default:
            change_data(node[node_sw][node_data][node_height], node_height, node[node_se])
        if node[node_nw][node_data][node_width] > default and node[node_ne][node_data][node_width] > default:
            node[node_data][node_width] = node[node_nw][node_data][node_width] + node[node_ne][node_data][node_width]
        if node[node_nw][node_data][node_height] > default and node[node_sw][node_data][node_height] > default:
            node[node_data][node_height] = node[node_nw][node_data][node_height] + node[node_sw][node_data][node_height]
    return node

def solveqtree(tree):
    result = []
    solve(tree, result)
    return result