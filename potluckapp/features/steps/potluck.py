@when(u'I go to the potluck app')
def step_impl(context):
    context.browser.get('http://localhost:5000')

@then(u'I should see the potluck app')
def step_impl(context):
    assert context.browser.title == "MangoPotluck"

@when(u'I submit the form with a valid event name')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')
    event = br.find_element_by_name['event_name']
    event.send_keys["Cornucopia"]
    br.find_element_by_id("createEvent").click()

@then(u'I should see the event page')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('eventpage')

@when(u'I submit a valid name and item name')
def step_impl(context):
    br = context.browser
    br.form['person'] = "David"
    br.form['body'] = "Fruit"
    br.find_element_by_id("additem").click()

@then(u'I should see the item displayed')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_name('body').text=="Fruit"

@when(u'I click delete')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('delete').click()

@then(u'I should no longer see the item displayed')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_name('body').text == []
    