LAB - Class 27
# Project: Django Models
**Author:** Michelle Salazar
----
## Problem Domain

### Model
<ul><li>create snack_tracker_project project
</li><li>This will involve some preliminary steps.
</li><li>Review previous class lab for details.
</li><li>create snacks app
</li><li>Add snacks app to project
</li><li>create Snack model
</li><li>make sure it extends from proper base class
</li><li>add name as a CharField with maximum length of 64 characters.
</li><li>add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
</li><li>from django.contrib.auth import get_user_model
</li><li>add description TextField
</li><li>add model to admin
</li><li>modify Snack model have user friendly display in admin
</li><li>create migrations and migrate data
</li><li>create a super user
</li><li>run development server
</li><li>Add a few snacks via Admin panel
</li><li>create another user and more snacks via Admin panel
</li><li>confirm that snacks behave as expected with proper name, purchaser and description.
</li><li>Looks like your model in good shape. Congrats!
</li></ul>

### Views for Snacks App
<ul><li>Where to create these views?</li>
<ul><li>Dig around and see if there’s a sensible spot.
</li><li> 

**HINT** There is one correct place for your app’s views.</li></ul>

<li>create SnackListView
</li>
<ul><li>extend ListView
</li><li>give a template of snack_list.html
</li><li>associate Snack model</li></ul>

<li>update url patterns for project
</li>
<ul><li>empty path should include snacks.urls
</li></ul>

<li>update snacks app urls</li><ul>
<li>empty sub-path should be handled by SnackListView</li></ul> 
<ul><li>Don’t forget to use as_view()</li></ul>


<li>add detail view</li><ul>
<li>link snack_detail.html template
</li><li>associate Snack model</li></ul>

<li>update app urlpatterns to handle detail view</li><ul>
</li><li>account for primary key in url
</li><li>path would look like localhost:8000/1/ to get to snack with id of 1</li></ul>
</li></ul>

### Templates
<ul><li>Addtemplates folder in root of project
</li><li>register templates folder in project settings TEMPLATES section
</li><li>create base.html ancestor template
</li><li>add main html document
</li><li>use Django Templating Language to allow child templates to insert content
</li><li>create snack_list.html template
</li><li>extend base template
</li><li>use Django Templating Language to display each snack’s name
</li><li>view home page (aka snack_list) and confirm snacks showing properly
</li><li>create snack_detail.html template
</li><li>template should extend base
</li><li>content should display snack’s name, description and purchaser
</li><li>add link in snack_list template to related detail page for each snack
</li><li>Add a link back to Home (aka snack_list) page from detail page.
</li><li>User Acceptance Tests
</li><li>Test Snack pages
</li></ul>

**NOTE** make sure test extends TestCase instead of SimpleTestCase used in previous class.
verify status code
verify correct template use
use url name instead of hard coded path

**TIP:** django.urls.reverse will help with that.
We can’t easily test SnackDetailView just yet.
Can you figure out why?

## Links and Resources

• back-end server url (when applicable)<br>

• front-end application (when applicable)

## Setup

cat requirements.txt
pip install pytest

**PORT -** Port Number

**DATABASE_URL -** URL to the running Postgres instance/db

*How to initialize/run your application (where applicable)*

• e.g. python main.py

## How to use your library (where applicable)

## Tests

• How do you run tests?
  
• Any tests of note?
  none

• Describe any tests that you did not complete, skipped, etc

## Links
---
*Notes:*
