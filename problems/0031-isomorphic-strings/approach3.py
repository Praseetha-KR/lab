class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def transform(string: str):
            index_mapping = {}
            res_arr = []
            for i, s in enumerate(string):
                if s not in index_mapping:
                    index_mapping[s] = i
                res_arr.append(str(index_mapping[s]))
            return " ".join(res_arr)
        return transform(s) == transform(t)
