var liElement = document.getElementById('186');

// Check if the element is found
if (liElement) {
  // Trigger a click on the element
  liElement.click();
  

  // Assuming there's a function contactDetail that updates 'email_head'
  // You may need to adjust this part based on your actual implementation
  var emailHead = document.getElementById('email_head').innerText; // Replace with the correct variable or property name
  console.log(emailHead);
} else {
  console.log('Element not found');
}