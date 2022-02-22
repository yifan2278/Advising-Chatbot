import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    inp = ""
    msgs = [["Nice to meet you!", "User"],["Hello!","Bot"],["Who are you?", "User"],["I am an advising chatbot.","Bot"]]
    ngOnInit(): void {
    }
    onGoToSubmit() {
      console.log("dnskjd")
    }
}
