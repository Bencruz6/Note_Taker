from django.shortcuts import redirect, render
from django.contrib import messages

from notes.form import NotesForm
from notes.models import Note

# Create your views here.

def home(request):
    """Display all notes and handle form submissions"""
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note created successfully!')
        else:
            messages.error(request, 'Error creating note. Please check your input.')
    
    notes = Note.objects.all().order_by('-created_at')
    form = NotesForm()
    return render(request, 'notes/index.html', {'notes': notes, 'form': form})


def delete_note(request, note_id):
    """Delete a note and return to home"""
    try:
        note = Note.objects.get(id=note_id)
        note.delete()
        messages.success(request, 'Note deleted successfully!')
    except Note.DoesNotExist:
        messages.error(request, 'Note not found.')
    
    return redirect('home')


def edit_note(request, note_id):
    """Edit a note and return to home"""
    try:
        note = Note.objects.get(id=note_id)
        if request.method == 'POST':
            form = NotesForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                messages.success(request, 'Note updated successfully!')
            else:
                messages.error(request, 'Error updating note. Please check your input.')
        else:
            form = NotesForm(instance=note)
        return render(request, 'notes/edit.html', {'form': form})
    except Note.DoesNotExist:
        messages.error(request, 'Note not found.')
        return redirect('home')
    except Note.DoesNotExist:
        messages.error(request, 'Note not found.')
    
    return redirect('home')
