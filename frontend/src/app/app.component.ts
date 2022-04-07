import { Component, ViewChild, ElementRef, AfterViewInit, NgModule, SimpleChanges } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  @ViewChild("scroll") scroll!: ElementRef;
  inp: String = ""
  msgs: String[][] = []
  postId: String = ""
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.msgs.push(["Nice to meet you!", "User"], ["Hello!", "Bot"], ["Who are you?", "User"], ["I am an advising chatbot.", "Bot"])
  }

  onGoToSubmit() {
    this.msgs.push([this.inp, "User"])
    this.http.post("http://localhost:8000", this.inp, { responseType: 'text' }).subscribe(data => {
      console.log("Response from server " + data)
      this.msgs.push([data, 'Bot'])
    })
    this.inp = ""
    let scrollInstance = this.scroll.nativeElement
    //auto scroll the chat window
    //scrollInstance.scrollTop = scrollInstance.children[this.msgs.length - 2].offsetHeight + scrollInstance.children[this.msgs.length - 2].offsetTop
    console.log(scrollInstance.children[this.msgs.length - 2])
    this.setView()
  }

  setView() {
    let scrollInstance = this.scroll.nativeElement
    let last = scrollInstance.children[scrollInstance.children.length - 1]
    console.log("ayay!!!")
    console.log(this.msgs)
    console.log(this.msgs.length)
    console.log(scrollInstance.children)
    console.log(scrollInstance.children.length)
    console.log(last)
    //last.scrollIntoView({ behavior: 'smooth' })
  }

  ngAfterViewChecked() {
    let len = this.scroll.nativeElement.children.length
    console.log(len)
    let last = this.scroll.nativeElement.children[len - 1]
    if (len != 4) {
      last.scrollIntoView({ behavior: 'smooth' })
    }
  }

}
