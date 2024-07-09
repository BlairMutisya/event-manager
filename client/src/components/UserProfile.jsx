// UserProfile.js
import React from "react";

function UserProfile() {
  // Example user data, replace with actual user data fetching logic
  const user = {
    username: "Blair",
    email: "blair@egmail.com",
  };

  return (
    <div className="user-profile">
      <h2>User Profile</h2>
      <p>Username: {user.username}</p>
      <p>Email: {user.email}</p>
      {/* Add more user-related details and functionalities here */}
    </div>
  );
}

export default UserProfile;
