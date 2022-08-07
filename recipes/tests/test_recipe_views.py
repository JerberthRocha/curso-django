from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_detail_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_category_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', args=(1,)))
        self.assertIs(view.func, views.category)
