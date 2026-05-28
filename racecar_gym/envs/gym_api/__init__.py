import os
from gymnasium.envs.registration import register

from .multi_agent_race import MultiAgentRaceEnv
from .changing_track import ChangingTrackSingleAgentRaceEnv, ChangingTrackMultiAgentRaceEnv
from .single_agent_race import SingleAgentRaceEnv
from .vectorized_multi_agent_race import VectorizedMultiAgentRaceEnv
from .vectorized_single_agent_race import VectorizedSingleAgentRaceEnv
from . import wrappers

base_path = os.path.dirname(__file__)
scenarios_dir = os.path.abspath(os.path.join(base_path, '..', '..', 'scenarios'))

def _register_multi_agent(name: str, file: str):
    scenario = os.path.join(scenarios_dir, file)
    register(
        id=name,
        entry_point='racecar_gym.envs.gym_api:MultiAgentRaceEnv',
        kwargs={'scenario': scenario}
    )

def _register_single_agent(name: str, file: str):
    scenario = os.path.join(scenarios_dir, file)
    register(
        id=name,
        entry_point='racecar_gym.envs.gym_api:SingleAgentRaceEnv',
        kwargs={'scenario': scenario}
    )

register(
    id='MultiAgentRaceEnv-v0',
    entry_point='racecar_gym.envs.gym_api:MultiAgentRaceEnv',
    kwargs={}
)

register(
    id='SingleAgentRaceEnv-v0',
    entry_point='racecar_gym.envs.gym_api:SingleAgentRaceEnv',
    kwargs={}
)

if os.path.exists(scenarios_dir):
    for scenario_file in os.listdir(scenarios_dir):
        if scenario_file.endswith('.yml'):
            track_name = os.path.basename(scenario_file).split('.')[0]
            name = f'{track_name.capitalize()}'
            _register_multi_agent(name=f'MultiAgent{name}-v0', file=scenario_file)
            _register_single_agent(name=f'SingleAgent{name}-v0', file=scenario_file)

__all__ = ["SingleAgentRaceEnv", "MultiAgentRaceEnv", "VectorizedSingleAgentRaceEnv", "VectorizedMultiAgentRaceEnv", "ChangingTrackSingleAgentRaceEnv", "ChangingTrackMultiAgentRaceEnv", "wrappers"]