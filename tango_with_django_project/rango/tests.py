from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from rango.models import Category, Page, Commit


def add_category(name, views=0, likes=0):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views
    category.likes = likes

    category.save()
    return category


def add_page(category, title, url, content):
    return Page.objects.get_or_create(category=category, title=title, url=url, content=content)[0]


class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        category = add_category('test', views=-1, likes=0)

        self.assertEqual((category.views >= 0), True)

    def test_slug_line_creation(self):
        category = add_category('Random Category String')
        category.save()

        self.assertEqual(category.slug, 'random-category-string')


class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('rango:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):
        add_category('Python', 1, 1)
        add_category('C++', 1, 1)
        add_category('Erlang', 1, 1)

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python')
        self.assertContains(response, 'C++')
        self.assertContains(response, 'Erlang')

        num_categories = len(response.context['categories'])
        self.assertEquals(num_categories, 3)


class PageAccessTests(TestCase):
    def test_page_content_ifempty(self):
        category = add_category('Python', 1, 1)
        page = add_page(category, 'Documentation', 'https://docs.python.org/3/', None)

        self.assertTrue(page.content is not None)


class CommentTests(TestCase):
    def test_every_comment_has_user_page(self):
        comment = Commit.objects.all()
        CountNum = 0
        for i in comment:
            if i.page_id & i.user_id is None:
                CountNum = CountNum + 1

        self.assertTrue(CountNum == 0)
