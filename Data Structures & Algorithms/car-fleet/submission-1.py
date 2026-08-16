class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # front-most car first
        
        fleets = 0
        last_time = 0.0  # time of the fleet currently ahead
        
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > last_time:      # can't catch the fleet ahead -> new fleet
                fleets += 1
                last_time = time      # this car now sets the pace for cars behind it
        
        return fleets