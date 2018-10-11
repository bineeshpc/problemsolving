
import random

class Human:
    def __init__(self, is_rationalist):
        self.is_rationalist = is_rationalist
        self.alive = True

    def rationalist(self):
        return self.is_rationalist

    def survive_predator_attack(self):
        if random.random() < .5:
            self.alive = False

    def go_to_predator(self):
        go_to_predator_value = random.random()
        if self.rationalist():
            value = go_to_predator_value > 0.1
        else:
            value = go_to_predator_value < 0.1
        if value:
            self.survive_predator_attack()
        #print "I am {} went to predator {} and {}".format(self.rationalist(), value, self.alive)
        return value

    def survive(self, signal):
        return not (signal.is_predator and self.go_to_predator() and self.alive)
            

def make_humans(n):
    humans = []
    for i in range(n):
        if i % 2 == 0:
            human = Human(is_rationalist=True)
        else:
            human = Human(is_rationalist=False)
        humans.append(human)
    return humans

class Signal:
    def __init__(self, is_predator):
        self.is_predator = is_predator


def make_signals(n):
    signals = []
    for _ in range(n):
        if random.random() < .5:
            signal = Signal(is_predator=True)
        else:
            signal = Signal(is_predator=False)
        signals.append(signal)
    return signals

def rationalist_count(humans):
    return len([human for human in humans if (human.rationalist() and human.alive)])

def believer_count(humans):
    return len([human for human in humans if (not human.rationalist() and human.alive)])


all_humans = make_humans(10**4 * 2)
all_signals = make_signals(10**1)

print ('rationalist count = ', rationalist_count(all_humans))
print ('believer count = ', believer_count(all_humans))

for human in all_humans:
    for signal in all_signals:
        human.survive(signal)

print ('rationalist count = ', rationalist_count(all_humans))
print ('believer count = ', believer_count(all_humans))
