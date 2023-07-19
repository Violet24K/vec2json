# vec2json
Converter from vector list to json format

Such convertion bridge the gaps in many repos, e.g. AAAI 2021 Dingal: Dynamic Knowledge Graph Alignment. (https://github.com/idea-reading-group/dingal)

### Basic Usage

#### Example

We used vec2json in a graph alignment scenario, where a whole graph and a sub graph exists. Sub-graph is a part of whole graph. These are only used to calculate the whole graph size (number of nodes), and can be revised for applications that are not within graph alignment scope.

To run our example, set the dataset_property.py file: DATASET_SIZE, SUB_SIZE, DATASET_NAME. The parameters we give are accurate and only need to be commented/uncommented.

    ```python3 generate_json.py```
