## dfs 
- 일반적으로 재귀함수로 구현
- 하나의 노드에서 막힐때까지 쭉 가본다음에 다시 돌아오는 방식
- 최단 경로 구할때는 좋지 않은거 같음.. => 모든 케이스에 대해 최솟값 비교 필요


## bfs
- 큐를 사용하여 구현(collections.deque)
- 하나의 노드에서 연결된 인접노드들을 모두 방문하는 방식
- 최솟값 구할때 좋음. => 현재값이 정답인 경우 그게 최솟값
