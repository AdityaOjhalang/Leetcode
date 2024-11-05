class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for astr in asteroids:
            if astr > mass:
                return False
            
            mass += astr
        return True