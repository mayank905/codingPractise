from typing import List

# def count_trailing_zeros(n):
#     count = 0
#     while n > 0 and n % 10 == 0:
#         count += 1
#         n //= 10
#     return count

# class Solution:
#     def isPossible(self, n : int, arr : List[int]) -> int:
#         # code here
#         prod=1
#         for i in range(n):
#             prod*=arr[i]
#         left=1
#         for i in range(n-1):
#             left*=arr[i]
#             right=prod//left
#             leftT=count_trailing_zeros(left)
#             rightT=count_trailing_zeros(right)
#             if leftT==rightT:
#                 return 1
#         return 0

class Solution:
    def get(self, n: int) -> [int, int]: # type: ignore
        cnt1 = 0
        while n % 2 == 0:
            n //= 2
            cnt1 += 1
        cnt2 = 0
        while n % 5 == 0:
            n //= 5
            cnt2 += 1
        return cnt1, cnt2

    def isPossible(self, n: int, arr: List[int]) -> int:
        aux = [[0, 0] for _ in range(n)]
        aux[n - 1] = list(self.get(arr[n - 1]))
        for i in range(n - 2, 0, -1):
            p = self.get(arr[i])
            q = aux[i + 1]
            aux[i] = [p[0] + q[0], p[1] + q[1]]

        ans = [0, 0]        
        for i in range(n - 1):
            x = self.get(arr[i])
            ans[0] += x[0]
            ans[1] += x[1]
            p = min(ans[0], ans[1])
            q = min(aux[i + 1][0], aux[i + 1][1])
            if p == q:
                return 1
        return 0
        
sol=Solution()
# n=4
# arr=[2,5,1,100]
# n=6
# arr=[23, 19, 16, 48, 11, 45]
n=197
sarr='391 205 499 325 327 211 178 435 233 319 131 337 489 286 359 242 133 153 119 333 216 423 174 256 492 206 122 140 475 466 462 209 221 208 139 275 396 190 357 131 126 402 308 123 364 222 388 332 208 477 247 146 448 203 108 108 343 177 227 311 483 373 285 119 478 352 226 377 220 178 135 323 203 235 396 129 290 403 185 433 255 192 143 410 481 144 478 322 240 178 262 197 188 442 428 439 123 410 242 154 357 270 236 144 363 222 212 210 363 283 264 231 185 352 258 307 351 220 253 488 417 199 371 269 405 408 461 476 299 111 232 107 406 402 374 232 345 377 337 182 488 150 219 422 113 425 129 172 444 231 402 448 151 179 252 332 374 455 272 462 495 303 166 305 436 471 214 130 409 437 169 236 368 313 387 221 155 212 500 297 357 299 392 330 390 232 420 312 132 254 185 192 135 219 373 246 389'
arr=[int(s) for s in sarr.split(' ')]
result=sol.isPossible(n,arr)
print(result)