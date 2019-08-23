from django.test import TestCase

# Create your tests here.
'''
<div class="admin_panel">
    <form name="productForm" method="POST" action="">
        <div class="formObject">
            {% csrf_token %}
            <label for="menu_id">Select a product from the list to edit:</label>
            <select id="menu_id" name="menu" onChange="top.location.href=this.options[this.selectedIndex].value;">
            {% for product in products %}
                <option value="../{{  allGroupSignedURL }}/details/">{{ allGroupSignedURL.name }}</option>
            {% endfor %}
            </select>
            <div class="fromBtn_container">
                <button type="button" class="btn"><a href="{% url 'createRecord' %}">Create New Product</a></button>
                <button type="button" class="btn"><a href="{% url 'home' %}">Logout of Profile</a></button>
            </div>
        </div>
    </form>
</div>

/views
def admin_console(request):
    products = Product.objects.all()
    return render(request, 'products/products_page.html', {'products': products})
'''