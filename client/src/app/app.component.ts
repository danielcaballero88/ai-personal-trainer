import { Component, OnInit } from '@angular/core'
import { RouterOutlet } from '@angular/router'
import { TrainerService } from './services/trainer.service'

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent implements OnInit {
  title = 'client'

  constructor(private trainer: TrainerService) {}

  ngOnInit(): void {
    this.trainer.connect()
  }
}
