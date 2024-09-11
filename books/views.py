
from flask import render_template, request, url_for,redirect
from app.books import book_blueprint
from app.models import Book ,db
from app.books.forms import BookForm, EditForm


@book_blueprint.route('',endpoint='landing')
def landing():
    books = Book.query.all()
    return render_template("books/landing.html", books=books)


@book_blueprint.route('/form/create',methods=["GET","POST"], endpoint='form_create' )
def create_book():
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print(request.form)

        book = Book(
        title=request.form["title"],
        description=request.form["description"],
        image=request.form["image"],
        num_pages=request.form["num_pages"]
        )
        db.session.add(book)
        db.session.commit()
        return redirect(book.show_url)
    return render_template("books/forms/create.html", form=form)


@book_blueprint.route('/<int:id>',endpoint='show')
def show(id):
    book = db.get_or_404(Book, id)
    return render_template("books/show.html", book=book)


@book_blueprint.route('/<int:id>/delete',endpoint='delete' ,methods=["POST"])
def delete(id):
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("books.landing"))



@book_blueprint.route('/<int:id>/edit', endpoint='edit', methods=['GET', 'POST'])
def edit(id):
    book = db.get_or_404(Book, id)
    form = EditForm(obj=book)

    if form.validate_on_submit():

        book.title = form.title.data
        book.description = form.description.data
        book.image = form.image.data
        book.num_pages = form.num_pages.data
        db.session.commit()
        return redirect(book.show_url)

    return render_template('books/forms/edit.html', form=form, book=book)
