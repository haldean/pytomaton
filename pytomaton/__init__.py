import collections
import inspect

class statemachine:
  def __init__(self):
    try:
      self._states = set(self.states)
    except NameError:
      raise Exception('No state list defined in state machine class')

    try:
      self._current_state = self.start_state
      if self._current_state not in self._states:
        raise Exception('Start state "%s" not defined in state list'
            % self._current_state)
    except NameError:
      raise Exception('No start_state defined in state machine class')

    def is_transition_func(func):
      return hasattr(func, '_pytomaton_transition_info')
    methods = inspect.getmembers(self, predicate=inspect.ismethod)
    methods = [x[1] for x in methods if is_transition_func(x[1])]

    self._transition_functions = collections.defaultdict(dict)
    for method in methods:
      from_state, to_state = method._pytomaton_transition_info
      self._transition_functions[to_state][from_state] = method

  def transition(self, to_state):
    if to_state in self._transition_functions:
      state_funcs = self._transition_functions[to_state]
      if self._current_state in state_funcs:
        state_funcs[self._current_state]()
      if None in state_funcs:
        state_funcs[None]()
    self._current_state = to_state

def on_transition(from_state, to_state):
  def func_decorator(func):
    func._pytomaton_transition_info = (from_state, to_state)
    return func
  return func_decorator

def on_enter(to_state):
  def func_decorator(func):
    func._pytomaton_transition_info = (None, to_state)
    return func
  return func_decorator
