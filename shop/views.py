from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def course_list(request, category_slug=None):
    coursecategory = None
    coursecategories = Coursecategory.objects.all()
    course = Course.objects.filter(available=True)
    if coursecategory_slug:
        coursecategory = get_object_or_404(Coursecategory, slug=coursecategory_slug)
        courses = courses.filter(coursecategory=coursecategory)
    return render(request, 'shop/courses/list.html', {'coursecategory': category,
                                                      'coursecategories': categories,
                                                      'courses': courses})

def course_detail(request, id, slug):
    course = get_object_or_404(Course, id=id, slug=slug, available=True)
    cart_course_form = CartAddCourseForm()
    return render(request,
                  'shop/course/detail.html',
                  {'course': course,
                   'cart_course_form': cart_course_form})