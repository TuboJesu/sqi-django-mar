window.onload = function() {
    // Set a timeout to show the popup after 3 seconds
    setTimeout(function() {
      // Create the modal container
      const modal = document.createElement('div');
      modal.style.position = 'fixed';
      modal.style.left = '0';
      modal.style.top = '0';
      modal.style.width = '100%';
      modal.style.height = '100%';
      modal.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
      modal.style.display = 'flex';
      modal.style.justifyContent = 'center';
      modal.style.alignItems = 'center';
      modal.style.zIndex = '1000';
  
      // Create the popup content
      const popupContent = document.createElement('div');
      popupContent.style.backgroundColor = 'white';
      popupContent.style.padding = '30px';
      popupContent.style.borderRadius = '5px';
      popupContent.style.width = '400px'; // Increased from 300px to 400px
      popupContent.style.textAlign = 'center';
      popupContent.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
      popupContent.style.position = 'relative'; // Added for positioning the close button
  
      // Create close button (X)
      const closeButton = document.createElement('div');
      closeButton.textContent = '×';
      closeButton.style.position = 'absolute';
      closeButton.style.top = '10px';
      closeButton.style.right = '15px';
      closeButton.style.fontSize = '24px';
      closeButton.style.fontWeight = 'bold';
      closeButton.style.color = '#aaa';
      closeButton.style.cursor = 'pointer';
      
      // Add hover effect to close button
      closeButton.onmouseover = function() {
        closeButton.style.color = '#333';
      };
      closeButton.onmouseout = function() {
        closeButton.style.color = '#aaa';
      };
      
      // Add event listener to close button
      closeButton.addEventListener('click', function() {
        document.body.removeChild(modal);
      });
  
      // Add title
      const title = document.createElement('h2');
      title.textContent = 'Subscribe to Our Newsletter';
      title.style.marginTop = '0';
      title.style.color = '#333';
      title.style.fontSize = '24px'; // Increased font size
  
      // Create input field
      const input = document.createElement('input');
      input.type = 'email';
      input.placeholder = 'Your email address';
      input.style.width = '100%';
      input.style.padding = '12px'; // Increased padding
      input.style.margin = '20px 0'; // Increased margin
      input.style.borderRadius = '3px';
      input.style.border = '1px solid #ddd';
      input.style.boxSizing = 'border-box';
      input.style.fontSize = '16px'; // Increased font size
  
      // Create submit button
      const button = document.createElement('button');
      button.textContent = 'Subscribe';
      button.style.backgroundColor = '#4CAF50';
      button.style.color = 'white';
      button.style.padding = '12px 20px'; // Increased padding
      button.style.border = 'none';
      button.style.borderRadius = '3px';
      button.style.cursor = 'pointer';
      button.style.fontWeight = 'bold';
      button.style.fontSize = '16px'; // Increased font size
      button.style.width = '100%'; // Make button full width
      
      // Add hover effect to button
      button.onmouseover = function() {
        button.style.backgroundColor = '#45a049';
      };
      button.onmouseout = function() {
        button.style.backgroundColor = '#4CAF50';
      };
      
      // Add event listener to button
      button.addEventListener('click', function() {
        if (input.value) {
          // Handle the email submission here
          console.log('Email submitted:', input.value);
          document.body.removeChild(modal);
        } else {
          // Add validation indicator
          input.style.border = '1px solid #f44336';
        }
      });
  
      // Add event listener to close when clicking outside the popup
      modal.addEventListener('click', function(event) {
        if (event.target === modal) {
          document.body.removeChild(modal);
        }
      });
      
      // Assemble the popup
      popupContent.appendChild(closeButton);
      popupContent.appendChild(title);
      popupContent.appendChild(input);
      popupContent.appendChild(button);
      modal.appendChild(popupContent);
      
      // Add to the document
      document.body.appendChild(modal);
      
      // Focus on the input field
      input.focus();
    }, 3000); // 3000 milliseconds = 3 seconds
  }