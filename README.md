pytomaton: State Machines in Python
=========

Example
-------

    import pytomaton

    class ConnectionMachine(statemachine):
      states = ['waiting_for_connection', 'waiting_for_ready', 'all_ready']
      start_state = 'state1'

      def on_connect(self):
        self.transition('waiting_for_ready')

      @on_transition('waiting_for_connection', 'waiting_for_ready')
      def send_ready_prompt(self):
        self.broadcast('are you ready?')

      def receive_ready_confirm(self):
        if self.all_ready():
          self.transition('all_ready')

      @on_enter('all_ready')
      def send_all_ready(self):
        self.broadcase('everyone is ready!')
