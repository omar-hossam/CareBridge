## Components

Add your components inside `app/templates/macros.html`

**Example:**

*macros.html*

```html
{% macro button(text, url="#") %}
  <a href="{{ url }}" role="button">{{ text }}</a>
{% endmacro %}

```

*file.html*

```html
{% from 'macros.html' import button %}

{{ button("Click Me", "/dashboard") }}
```

- [ ] Responsive Navbar for anyone not logged in
- [ ] Individual Navbars for Donors, Hospitals and Admins  
- [ ] Reusable Sidebar connected with navbars smoothly

## Pages

- [ ] homepage (navbar, hero, short about, how it works, get started, footer)
- [ ] about page
- [ ] requests (refers to requested donations either from hospitals or direct for people)
- [ ] request help (for direct donation help) **no need for signin but donors, hospitals can't access it**

### Donors

- [ ] dashboard 
- [ ] donate page 
- [ ] payment confirmation page
- [ ] settings

### Hospitals

- [ ] dashboard
- [ ] request donations
- [ ] settings
