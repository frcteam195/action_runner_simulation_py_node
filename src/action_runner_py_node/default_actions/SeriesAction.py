from action_runner_py_node.default_actions.Action import Action
from datetime import datetime
from typing import List
import rospy

class SeriesAction(Action):
    def __init__(self, action_list:List[Action]):
        self.__current_action_index:int = -1
        self.__action_list:List[Action] = action_list

        for a in self.__action_list[:]:
            if a is None:
                print("Invalid action added to list")
                self.__action_list.remove(a)

        self.__current_action:Action = None
        pass

    def start(self):
        self.__current_action = None
        self.__current_action_index = 0

    def update(self):
        if self.__current_action == None:
            if self.__current_action_index >= len(self.__action_list):
                return

            self.__current_action = self.__action_list[self.__current_action_index]
            self.__current_action_index += 1
            self.__current_action.start()

        self.__current_action.update()

        if self.__current_action.isFinished():
            self.__current_action.done()
            self.__current_action = None

    def done(self):
        pass

    def isFinished(self) -> bool:
        return self.__current_action == None and self.__current_action_index == len(self.__action_list)