#!/bin/python3
def get_abbr_num_str(n):
    big_numbers_to_letters = {
        1: '',
        1000: 'K',
        1000000: 'M',
        1000000000: 'B',
        1000000000000: 'T',
        1000000000000000: 'Q'
    }

    big_number = 1
    factor = 1000
    base = n

    while base >= factor:
        base = base // factor
        big_number *= factor
    
    assert base * big_number == n
    letter = big_numbers_to_letters[big_number]
    return f'{base}{letter}'

def assert_with_prints(value, target, value_title):
    assert value == target, f'{value_title} is not {target}'
    print(f'success, {value_title} = {target}')

def species_to_full_name(species):
    if 'syeast' in species:
        return species
    else:
        return f'IID{species}'

def calc_f1(orth, found, n):
    tp = orth
    fp = found - orth
    fn = n - orth
    return tp / (tp + 0.5 * (fp + fn))

def print_dict(d):
    print('\n'.join([f'{k}\t{v}' for k, v in d.items()]))

def order_gtags(gtag1, gtag2):
    from graph_helpers import get_graph_path, read_in_nodes, read_in_el
    graph_path1 = get_graph_path(gtag1)
    graph_path2 = get_graph_path(gtag2)
    nodes1 = read_in_nodes(graph_path1)
    nodes2 = read_in_nodes(graph_path2)
    el1 = read_in_el(graph_path1)
    el2 = read_in_el(graph_path2)
    num_nodes1 = len(nodes1)
    num_nodes2 = len(nodes2)
    num_edges1 = len(el1)
    num_edges2 = len(el2)

    if num_nodes1 < num_nodes2:
        return (gtag1, gtag2)
    elif num_nodes2 < num_nodes1:
        return (gtag2, gtag1)
    else:
        if num_edges1 <= num_edges2:
            return (gtag1, gtag2)
        else:
            return (gtag2, gtag1)

if __name__ == '__main__':
    assert_with_prints(5, 5, 'foo')
