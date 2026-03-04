class vehicle:
    def __init__(self, name, speed = 0, booms = str):
        self.name = name
        self.speed = speed
        self.booms = booms   
    def is_it_electric():
        print("is it electric?")
        o = input()
        o = o.strip()
        o = o.lower()
        if o == "yes":
            return True
        else:
            return False
    
    def does_it_boom():
        y = is_it_electric()
        if y == True:
                self.booms = "high"
        else:
                self.booms = "low"
    def how_fast(self):
        print(f"Car goes brrrrr, or {self.speed} km/h" )
    def go_brrr(self, delta_speed):
        self.speed += delta_speed
    def no_go_brrr(self, delta_speed):
        self.speed -= delta_speed
    def __str__(self):
        return f"This f{self.name} goes brrrr at {self.speed}. It's chance of boom is {self.booms}"
    
    class car(vehicle):
        def __init__(self, name, speed = 0, booms = str, wheelcount = 4):
            self.name = name
            self.speed = speed
            self.booms = booms   
            self.wheel_count = wheelcount
        def engineSound():
            print("BRRRRRRRR")
            class SUV(car(vehicle)):
            def __init__(self, name, speed = 0, booms = str, wheelcount = 4, offroadness = "YES"):
                self.wheel_count = wheelcount
                self.name = name
                self.speed = speed
                self.booms = booms   
                self.offroadness = offroadness
            def engineSound():
                print("LOUDER BRRRRRRRRR")