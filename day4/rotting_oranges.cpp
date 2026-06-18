#include <vector>
#include <queue>

class Solution {
public:
    int orangesRotting(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        std::queue<std::pair<int, int>> q;
        int fresh_count = 0;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    fresh_count++;
                } else if (grid[i][j] == 2) {
                    q.push({i, j});
                }
            }
        }

        if (fresh_count == 0) return 0;

        int minutes_passed = 0;
        std::vector<std::pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while (!q.empty() && fresh_count > 0) {
            int current_queue_size = q.size();
            minutes_passed++; 

            for (int i = 0; i < current_queue_size; ++i) {
                auto [r, c] = q.front();
                q.pop();

                for (auto [dr, dc] : directions) {
                    int nr = r + dr;
                    int nc = c + dc;

                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2; 
                        q.push({nr, nc}); 
                        fresh_count--;  
                    }
                }
            }
        }
        return fresh_count == 0 ? minutes_passed : -1;
    }
};
