import fischertechnik.factories as txtFactory
txtController = txtFactory.controller_factory.create_graphical_controller()
O1 = txtFactory.output_factory.create_lamp(txtController, 1)
O2 = txtFactory.output_factory.create_lamp(txtController, 2)
