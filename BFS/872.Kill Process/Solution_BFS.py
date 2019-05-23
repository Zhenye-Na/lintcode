from collections import defaultdict, deque


class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """
    def killProcess(self, pid, ppid, kill):
        # Write your code here
        processes = []
        if not pid or not ppid or len(pid) == 0 or len(ppid) == 0:
            return processes

        process_graph = self._create_graph(pid, ppid)

        queue = deque([kill])
        history = set([kill])

        while queue:
            process = queue.popleft()
            processes.append(process)

            for child_p in process_graph[process]:
                if child_p in history:
                    continue

                queue.append(child_p)

        return processes



    def _create_graph(self, pid, ppid):
        graph = defaultdict(list)
        for _pid, _ppid in zip(pid, ppid):
            graph[_ppid].append(_pid)

        return graph
