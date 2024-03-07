lass Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        l = 0
        for r in range(len(arr)):
            if arr[r] != arr[l]:
                arr[l+1] = arr[r]
                l += 1
                print(l)  # Debug: print current unique element index
                print(arr)  # Debug: print current state of array
        return l + 1  # Return count of unique elements
