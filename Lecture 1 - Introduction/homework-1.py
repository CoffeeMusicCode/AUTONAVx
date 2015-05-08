import quadrotor.command as cmd
from math import sqrt

def plan_mission(mission):

    commands  = [
        cmd.up(1),
        cmd.forward(1),
        cmd.right(2),
        cmd.forward(4),
        cmd.left(4),
        cmd.backward(4),
        cmd.turn_right(45),
        cmd.forward(3),
    ]

    mission.add_commands(commands)
