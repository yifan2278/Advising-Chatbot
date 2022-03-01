import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdvanceViewComponent } from './advance-view.component';

describe('AdvanceViewComponent', () => {
  let component: AdvanceViewComponent;
  let fixture: ComponentFixture<AdvanceViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdvanceViewComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AdvanceViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
