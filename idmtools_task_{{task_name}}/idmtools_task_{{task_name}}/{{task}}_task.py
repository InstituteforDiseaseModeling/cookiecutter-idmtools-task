import json
from dataclasses import dataclass, field
from functools import partial
from logging import getLogger, DEBUG
from typing import Union, Dict, Any
from idmtools.assets import Asset, AssetCollection
from idmtools.entities.itask import ITask
from idmtools.entities.simulation import Simulation
from idmtools.registry.task_specification import TaskSpecification

TJSONConfigKeyType = Union[str, int, float]
TJSONConfigValueType = Union[str, int, float, Dict[TJSONConfigKeyType, Any]]

logger = getLogger(__name__)
user_logger = getLogger('user')


@dataclass
class {{task_name}}Task(ITask):
    """
    Defines an extensible simple task that implements functionality through optional supplied use hooks
    """

    # TODO Implement your properties on your task

    def __post_init__(self):
        super().__post_init__()
        # TODO Implment

    def gather_common_assets(self) -> AssetCollection:
        """
        Gather assets
        :return:
        """
        # TODO Implement your assets gathers
        return self.common_assets

    def gather_transient_assets(self) -> AssetCollection:
        """
        Gather transient assets
        """
        # TODO add transient assets like per simulations configuration, data, etc
        return self.transient_assets


    # Recommended method to implement. Some form of callback that can be used be sweeps
    # def set_parameter(self, key, value):
    #     """
    #     Update a parameter.
    #
    #     Args:
    #         key: Config
    #         value:
    #
    #     Returns:
    #
    #     """
    #
    #
    # @staticmethod
    # def set_parameter_sweep_callback(simulation: Simulation, param: str, value: Any) -> Dict[str, Any]:
    #     if not hasattr(simulation.task, 'set_parameter'):
    #         raise ValueError("update_task_with_set_parameter can only be used on tasks with a set_parameter")
    #     return simulation.task.set_parameter(param, value)
    #
    # @classmethod
    # def set_parameter_partial(cls, parameter: str):
    #     return partial(cls.set_parameter_sweep_callback, param=parameter)

    def pre_creation(self, parent: Union['Simulation', 'WorkflowItem']):
        # TODO oiptional method called before simulation or workflow item is created
        # Useful for variable command lines, or heavy processing you want to delay to last possible instance
        pass

    def __repr__(self):
        """
        String representation
        :return:
        """
        # TODO, implement string representation. It is could to include unique data here that distinguishes each instance of task
        return f"<{{task_name}} properties>"




class {{task_name}}TaskSpecification(TaskSpecification):

    def get(self, configuration: dict) -> {{task_name}}Task:
        return {{task_name}}Task(**configuration)

    def get_description(self) -> str:
        return "Defines a general command that has a simple JSON based config"
