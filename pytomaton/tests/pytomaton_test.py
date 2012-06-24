import unittest
from pytomaton import *

class SimpleAutomaton(statemachine):
  states = ['state1', 'state2']
  start_state = 'state1'

  @on_transition('state1', 'state2')
  def state1_to_state2(self):
    self.test_success_1 = True
    self.transition('state1')

  @on_enter('state1')
  def enter_state1(self):
    self.test_success_2 = True


class SimpleAutomatonTest(unittest.TestCase):
  def test_transition(self):
    myt = SimpleAutomaton()
    myt.transition('state2')

    self.assertTrue(myt.test_success_1)
    self.assertTrue(myt.test_success_2)

def test():
  unittest.main()
