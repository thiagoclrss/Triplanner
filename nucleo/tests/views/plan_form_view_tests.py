

from nucleo.views import PlanFormView


def test_check_plan_view_context(rf):
    request = rf.get('/')
    view = PlanFormView()
    view.setup(request)

    context = view.get_context_data()
    assert 'form' in context
