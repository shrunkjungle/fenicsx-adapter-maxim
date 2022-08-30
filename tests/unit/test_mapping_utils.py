import unittest
from unittest.mock import MagicMock
from unittest import TestCase
import numpy as np
from mpi4py import MPI
from dolfinx.mesh import create_unit_square
from dolfinx.fem import Function, FunctionSpace, VectorFunctionSpace


class TestAdapterCore(TestCase):
    def test_precompute_eval_vertices(self):
        """
        Test cell collision computation for function evaluation on vertices
        """

        from fenicsxprecice.mapping_utils import precompute_eval_vertices

        mesh = create_unit_square(MPI.COMM_WORLD, 2, 2)  # create dummy mesh

        # scalar valued
        V = FunctionSpace(mesh, ('P', 2))  # Create function space using mesh

        fenicsx_function = Function(V)
        fenicsx_function.interpolate(lambda x: x[0] + x[1]*x[1])

        precice_vertices = np.array([[0.5, 0.5, 0.0],
                                     [0.2, 0.2, 0.0]])
        expected_data = np.array([0.75, 0.24]).reshape((2, 1))

        cells = precompute_eval_vertices(precice_vertices, mesh)
        data = fenicsx_function.eval(precice_vertices, cells)
        np.testing.assert_almost_equal(data, expected_data)
