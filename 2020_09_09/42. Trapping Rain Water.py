class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        heightest_idx = 0
        total_area = 0

        # 计算总面积，找到最高的柱子
        for idx, h in enumerate(height):
            total_area += h
            if h > height[heightest_idx]:
                heightest_idx = idx

        # 柱子图的凸壳面积
        area_convex = 0

        # 左到最高
        max_h = 0
        for i in range(0, heightest_idx):
            max_h = max(height[i], max_h)
            area_convex += max_h

        # 右到最高
        max_h = 0
        for i in reversed(range(heightest_idx, n)):
            max_h = max(height[i], max_h)
            area_convex += max_h

        return area_convex - total_area