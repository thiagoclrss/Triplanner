from nucleo.views.plan_with_weights_view import (PlanWithWeightsFormView, PesosPlanosForm)


def test_check_context(rf):
    request = rf.get('/pesos/')
    view = PlanWithWeightsFormView()
    view.setup(request)

    context = view.get_context_data()
    assert 'form' in context
