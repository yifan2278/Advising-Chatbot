import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    inp = ""
    msgs = [["Nice to meet you!", "User"],["Hello!","Bot"],["Who are you?", "User"],["I am an advising chatbot.","Bot"]]
    postId = ""
    constructor(private http: HttpClient){}
    ngOnInit(): void {
    }
    
    onGoToSubmit() {
      this.msgs.push([this.inp, "User"])
      this.inp = ""
      this.http.post<any>('https://google.com', { title: 'Angular POST Request Example' }).subscribe(data => {
        this.postId = data.id;
      })
      console.log(this.postId)
    }


}
