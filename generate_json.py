import pdb
from dataset_property import DATASET_SIZE, SUB_SIZE, DATASET_NAME
node2vec_file = open('node2vec_' + DATASET_NAME + '.txt', 'r')
json_file = open(DATASET_NAME + '_vectorList.json', 'w')
all_lines = node2vec_file.readlines()
node2vec_file.close()
first_line = all_lines[0] 
items = first_line.strip().split(' ')
num_nodes = int(items[0])
dimensions = int(items[1])
node_list = []
node_emb_dict = {}
json_file.write('[')
for line_index in range(1, 1 + num_nodes):
    items = all_lines[line_index].strip().split(' ')
    node_id = int(items[0])
    node_list.append(node_id)
    emb = '['
    for j in range(1, dimensions):
        emb += items[j]
        emb += ','
    emb += items[dimensions]
    emb += ']'
    node_emb_dict[node_id] = emb

# create a sentinel
emb_sentinel = '['
for j in range(1, dimensions):
    emb_sentinel += '0.0'
    emb_sentinel += ','
emb_sentinel += '0.0'
emb_sentinel += ']'

node_list.sort()
# pdb.set_trace()

gen_size = DATASET_SIZE + SUB_SIZE
for node_index in range(gen_size - 1):
    try:
        json_file.write(node_emb_dict[node_index])
    except KeyError:
        json_file.write(emb_sentinel)
    json_file.write(',')

try:
    json_file.write(node_emb_dict[gen_size - 1])
except KeyError:
    json_file.write(emb_sentinel)

json_file.write(']')