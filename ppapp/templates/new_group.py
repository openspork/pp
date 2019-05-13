{% extends "base.j2" %}
{% block title %}
New Group
{% endblock %}
{% block content %}

    <form action="" method="post">
        {{ form.hidden_tag() }}
        <p>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}
        </p>
        <p>
            {{ form.note.label }}<br>
            {{ form.note(size=32) }}
        </p>
        <p>{{ form.submit() }}</p>
    </form>

{% endblock %}