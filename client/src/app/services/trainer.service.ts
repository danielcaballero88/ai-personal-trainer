import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { WebSocketSubject, webSocket } from 'rxjs/webSocket';
import { Observable } from 'rxjs';

const apiUrl = 'ws://localhost:8000/ws/123';

@Injectable({
  providedIn: 'root',
})
export class TrainerService {
  private socket$: WebSocketSubject<object>;

  constructor(private http: HttpClient) {
    this.socket$ = webSocket(apiUrl);
  }

  // Connect to the WebSocket
  connect(): void {
    this.socket$.subscribe({
      next: (msg) => console.log('message received: ' + msg), // Called whenever there is a message from the server.
      error: (err) => console.log(err), // Called if at any point WebSocket API signals some kind of error.
      complete: () => console.log('complete'), // Called when connection is closed (for whatever reason).
    });
  }

  // Disconnect from the WebSocket
  disconnect(): void {
    this.socket$.complete();
  }

  // Send a message to the WebSocket
  sendMessage(message: string): void {
    this.socket$.next({ message: 'Hello there' });
  }

  // Listen for incoming messages from the WebSocket
  getListener(): Observable<object> {
    return this.socket$.asObservable();
  }
}
