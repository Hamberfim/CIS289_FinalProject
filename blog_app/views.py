from django.shortcuts import render
from django.shortcuts import redirect
from .models import Topic
from .forms import TopicForm
from .forms import EntryForm


# Create your views here.
def index(request):
    """The home page for dj_blog_app."""
    return render(request, 'blog_app/index.html')


def topics(request):
    """Show All the Blog Topics"""
    topics = Topic.objects.order_by('date_added')
    content = {"topics": topics}
    return render(request, 'blog_app/blog_topics.html', content)


def topic(request, topic_id):
    """Show a Single Blog Topic and all its Blog Entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    content = {"topic": topic, "entries": entries}
    return render(request, 'blog_app/blog_topic.html', content)


def new_topic(request):
    """add new topic - by a user"""
    if request.method != 'POST':
        # if no data is submitted create a blank form
        form = TopicForm()
    else:
        # else submit data and process form
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_app:topics')

    # display a blank or an invalid form
    content = {'form': form}
    return render(request, 'blog_app/new_topic.html', content)


def new_entry(request, topic_id):
    """Add a new entry for a particular blog topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('blog_app:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    content = {'topic': topic, 'form': form}
    return render(request, 'blog_app/new_entry.html', content)


def edit_entry(request, entry_id):
    """Edit an existing blog entry."""
    entry = EntryForm.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_app:topic', topic_id=topic.id)

    content = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'blog_app/edit_entry.html', content)
