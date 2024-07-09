import React from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import "../styles.css"; // Your custom CSS for styling
import ProjectImage from "../Assets/project.jpg"; // Import the image
import ContactUs from "./Contact"; // Import the ContactUs component

function Home() {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
  };

  return (
    <div className="home-page">
      <div className="centered-container">
        <div className="welcome-section">
          <h1>
            Discover, create, and manage your events effortlessly with our
            intuitive platform.
          </h1>
          <p>Your ultimate platform for managing events.</p>
          <div className="buttons">
            <button className="explore-btn">Explore Events</button>
            <button className="dashboard-btn">Go to Dashboard</button>
          </div>
        </div>
      </div>

      <div className="features-section">
        <img src={ProjectImage} alt="Project" className="feature-image" />
        <div className="feature-content">
          <h2>Why Choose Us?</h2>
          <div className="feature">
            <div className="feature-icon">
              <i className="fas fa-calendar-check"></i>
            </div>
            <div className="feature-text">
              <h3>Efficient Event Management</h3>
              <p>
                Streamline event planning, scheduling, and attendee management.
              </p>
            </div>
          </div>
          <div className="feature">
            <div className="feature-icon">
              <i className="fas fa-users"></i>
            </div>
            <div className="feature-text">
              <h3>Engage with Attendees</h3>
              <p>
                Enhance attendee engagement with interactive features and
                notifications.
              </p>
            </div>
          </div>
          <div className="feature">
            <div className="feature-icon">
              <i className="fas fa-chart-line"></i>
            </div>
            <div className="feature-text">
              <h3>Analyze Event Success</h3>
              <p>Track metrics and analyze data to improve future events.</p>
            </div>
          </div>
        </div>
      </div>

      <div className="centered-container">
        <div className="card-slider">
          <Slider {...settings}>
            <div className="card">
              <h3>Event Title 1</h3>
              <p>
                Description: Lorem ipsum dolor sit amet, consectetur adipiscing
                elit.
              </p>
              <p>Date: 2024-07-15</p>
              <p>Location: New York City</p>
            </div>
            <div className="card">
              <h3>Event Title 2</h3>
              <p>
                Description: Sed do eiusmod tempor incididunt ut labore et dolore
                magna aliqua.
              </p>
              <p>Date: 2024-08-01</p>
              <p>Location: Los Angeles</p>
            </div>
            {/* Add more slides as needed */}
          </Slider>
        </div>
      </div>

     
      

      <footer className="footer">
        <p>&copy; 2024 Event Hive. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default Home;
