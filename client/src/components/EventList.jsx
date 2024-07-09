// EventList.js
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import EventCard from './EventCard';

const EventList = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    // Fetch events from API
    fetch('http://localhost:5000/events')
      .then(response => response.json())
      .then(data => setEvents(data))
      .catch(error => console.error('Error fetching events:', error));
  }, []);

  const handleDeleteEvent = eventId => {
    // Implement delete logic here
    console.log('Deleting event with ID:', eventId);
    // Example: You can perform a DELETE request to the API
  };

  return (
    <div className="event-list">
      <h2>Explore Events</h2>
      <div className="card-slider">
        <div className="card-container">
          {events.map(event => (
            <EventCard key={event.id} event={event} onDelete={handleDeleteEvent} />
          ))}
        </div>
      </div>
      <Link to="/event/new" className="submit">Create New Event</Link>
    </div>
  );
};

export default EventList;
